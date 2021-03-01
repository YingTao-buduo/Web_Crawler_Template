import get_source_data as source_data_getter
import write_2_excel as data_writer

my_url = ''  # target url
my_path = ''  # write path
my_filename = ''  # your filename


def start(url, path, filename):
    data = source_data_getter.get(url)

    while data is None or data is 'error':
        print('request failed, input \'Enter\' to retry')
        a = input()
        data = source_data_getter.get(url)
    while data is 'ERR:403':
        print('request failed, input \'Enter\' to retry')
        a = input()
        data = source_data_getter.get(url)
    while data is 'ERR:404':
        print('request failed, input \'Enter\' to retry')
        a = input()
        data = source_data_getter.get(url)

    print('Get web page successfully. URL: ' + url)

    try:
        # write your data to excel
        print('write' + + 'successfully')
    except BaseException:
        print('!!!Get web page failed. URL: ' + url)
        print('write' + + 'failed')
        print('1. input \'save\' to save file')
        print('2. input \'restart\' to continue')
        next = input()
        if next == 'save':
            workbook.save(path + '/' + filename + '.xlsx')
            print(filename + '.xlsx saved')
        if next == 'restart':
            write(data, path, filename)
        return


if __name__ == '__main__':
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    start(my_url, my_path, my_filename)
    workbook.save(path + '/' + filename + '.xlsx')
    print('Done')
