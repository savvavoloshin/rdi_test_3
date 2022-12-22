
import re
import os
import csv

def extractFilename(line):
    m = re.match("(\w+-\d+).*", line)
    if(m):
        return m.group(1)
    return line

def getTrns(line):
    # Аня_2500_5-148	[pau] Слушаю Бутусова и думаю о тебе [dot] [pau]

    line_words = line.split()
    good_words = []
    for word in line_words:
        if(re.match("(\w+\-\d+).*", word)):
            continue
        if("[pau]" in word):
            continue
        if("[dot]" in word):
            continue
        if("[spk]" in word):
            continue
        if("[quest]" in word):
            continue
        if("[fil]" in word):
            continue
        if("[dots]" in word):
            continue
        if("[excl]" in word):
            continue

        word = re.sub("\*","",word)
        word = re.sub("\:","",word)
        word = re.sub("\-","",word)
        
        good_words.append(word)

    return " ".join(good_words)

def main():

    dev_path = r'Dataset/dev'
    test_path = r'Dataset/test'
    train_path = r'Dataset/train'

    dev_filenames = os.listdir(dev_path)
    test_filenames = os.listdir(test_path)
    train_filenames = os.listdir(train_path)

    lines = []

    with open('Dataset/texts') as f:
        lines = f.readlines()

    def prepare_csv(filenames, path, lines, output_filename):
        csv_data = []
        for fn in filenames:
            for line in lines:
                if (re.sub("\.\w*","",fn) == extractFilename(line)):
                    filesize = os.stat("{0}/{1}".format(path, fn)).st_size
                    translation = getTrns(line)
                    csv_data.append([fn, filesize, translation.lower()])
        with open(output_filename, 'w') as file:
            writer = csv.writer(file)
            csv_header = ['wav_filename', 'wav_filesize', 'transcript']
            writer.writerow(csv_header)
            writer.writerows(csv_data)
    
    prepare_csv(dev_filenames, dev_path, lines, 'dev.csv')
    prepare_csv(test_filenames, test_path, lines, 'test.csv')
    prepare_csv(train_filenames, train_path, lines, 'train.csv')

if __name__ == '__main__':
    main()