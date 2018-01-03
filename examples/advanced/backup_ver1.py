import os
import time

# 1. 需要备份的文件与目录将被指定在一个列表中。
# Mac OS X 与 Linux 下：
source = ['/Users/support/Documents/projectRes/documents/notes']
# 注意：必须在字符串中使用双引号用以括起其中包含空格的名称。

# 2. 备份文件必须存储在一个主备份目录中
# Mac OS X 与 Linux 下：
target_dir = '/Users/support/Documents/projectRes/documents/backup'

# 3. 备份文件将打包压缩成 zip 文件。
# 4. zip 压缩文件的文件名由当前日期与时间构成。
"""
注意 os.sep 变量的使用方式——它将根据你的操作系统给出相应的分隔符，在 GNU/Linux 与 Unix 中它会是 '/'，在 Windows 中它会是 '\\'，在 Mac OS 中它会是 ':'。
使用 os.sep 而非直接使用这些字符有助于使我们的程序变得可移植，从而可以在上述这些系统中都能正常工作。
"""
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)    # 创建目录

# 5. 使用 zip 命令将文件打包成 zip 格式
# -r 选项用以指定 zip 命令应该递归地（Recursively）对目录进行工作，也就是说它应该包括所有的子文件夹与其中的文件
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
# os.system 函数可以使命令像是从系统中运行的，也就是说，从 shell 中运行的，
# 如果运行成功，它将返回 0，如果运行失败，将返回一个错误代码。
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')