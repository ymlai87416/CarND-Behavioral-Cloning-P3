import traceback
from string import Template
import os
import logging
import sys
import csv
from PIL import Image
from shutil import copyfile



class Application:
    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not Application.instance:
            Application.instance = Application.__ApplicationInner()
        return Application.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

    class __ApplicationInner:


        def __init__(self):
            self.logger = logging.getLogger("CarND-Behavioral-Cloning-P3")
            self.logger.setLevel(logging.INFO)
            handler = logging.FileHandler('application.log')
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

            # redirect stdout
            sys.stdout = open('stdout.log', 'w')
            sys.stderr = open('stderr.log', 'w')

        @property
        def logger(self):
            return self.__logger

        @logger.setter
        def logger(self, logger):
            self.__logger = logger

        def cloneFrom(self, src, dst, start, end):
            image_src_dir = os.path.join(src, "IMG")
            src_csv_flname = os.path.join(src, "driving_log.csv")

            image_dst_dir = os.path.join(dst, "IMG")
            dst_csv_flname = os.path.join(dst, "driving_log.csv")

            if (os.path.isdir(src) and os.path.isfile(src_csv_flname) and os.path.isdir(image_src_dir)):
                if (os.path.isdir(dst)):
                    # create a empty directory
                    if (os.path.isfile(dst_csv_flname) and os.path.isdir(image_dst_dir)):
                        lines_dst = self.readTrainData(dst)
                    else:
                        self.initTrainDir(dst)

                elif os.path.isfile(dst):
                    raise Exception("Destination must be a file")
                else:
                    # append it to the target and write it to the disk
                    self.initTrainDir(dst)
                    lines_dst = []

                lines_src = self.readTrainData(src)
                lines_copy = lines_src[start:end]
                for line in lines_copy:
                    for i in range(3):
                        try:
                            picture_src = line[i]
                            head, tail = os.path.split(picture_src)
                            picture_dst = os.path.join(image_dst_dir, tail)
                            line[i] = picture_dst
                            copyfile(picture_src, picture_dst)
                        except Exception:
                            self.logger.error("Error when deleting file.", exc_info=True)
                lines_dst = lines_dst + lines_copy
                self.writeTrainData(dst, lines_dst)
            else:
                raise Exception("Source is not a proper train data directory.")

        def removeFrom(self, src, start, end):
            image_dir = os.path.join(src, "IMG")
            csv_flname = os.path.join(src, "driving_log.csv")
            if (os.path.isdir(src) and os.path.isfile(csv_flname) and os.path.isdir(image_dir)):
                # read the file
                lines_src = self.readTrainData(src)
                lines_del = lines_src[start:end]
                for line in lines_del:
                    for i in range(3):
                        try:
                            picture = line[i]
                            os.remove(picture)
                        except Exception:
                            self.logger.error("Error when deleting file.", exc_info=True)

                del lines_src[start:end]
                self.writeTrainData(src, lines_src)
            else:
                raise Exception("Source is not a proper train data directory.")

        def fixImageLink(self, src):
            image_dir = os.path.join(src, "IMG")
            csv_flname = os.path.join(src, "driving_log.csv")
            if (os.path.isdir(src) and os.path.isfile(csv_flname) and os.path.isdir(image_dir)):
                lines_src = self.readTrainData(src)

                for line in lines_src:
                    for i in range(3):
                        try:
                            picture = line[i]
                            if("/" in picture):
                                filename = picture.split('/')[-1]
                                picture = os.path.join(image_dir, filename)
                                line[i] = picture
                            else:
                                filename = picture.split('\\')[-1]
                                picture = os.path.join(image_dir, filename)
                                line[i] = picture
                        except Exception:
                            self.logger.error("Error when deleting file.", exc_info=True)

                self.writeTrainData(src, lines_src)
            else:
                raise Exception("Source is not a proper train data directory.")

        # read the csv file
        def readTrainData(self, src_dir):
            lines = []
            csv_filep = os.path.join(src_dir, "driving_log.csv")
            with open(csv_filep, newline ='\n') as csvfile:
                reader = csv.reader(csvfile)
                for line in reader:
                    lines.append(line)

            return lines

        def writeTrainData(self, dst_dir, lines):
            try:
                csv_filep = os.path.join(dst_dir, "driving_log.csv")
                with open(csv_filep, 'w', newline ='\n') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    #for line in lines:
                    writer.writerows(lines)
            except Exception as ex:
                self.logger.error("Error when writing file", exc_info=True)


        # create a empty directory
        def initTrainDir(self, dir):
            image_dir = os.path.join(dir, "IMG")
            csv_flname = os.path.join(dir, "driving_log.csv")

            if not os.path.exists(image_dir):
                os.makedirs(image_dir)

            with open(csv_flname, 'a'):
                os.utime(csv_flname, None)

        def fixImagePath(self, dir):
            lines = self.readTrainData(dir)
            for line in lines:
                for i in range(3):
                    picture_src = line[i]
                    head, tail = os.path.split(picture_src)
                    picture_dst = os.path.join(dir, tail)
                    line[i] = picture_dst

            self.writeTrainData(dir, lines)