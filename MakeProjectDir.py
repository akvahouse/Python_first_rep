import os
path = r'D:\Work'
folders = ['Source',
           'Exit']

def createFolder(path):
  if not os.path.exists(path):
    os.mkdir(path)

dayMonday = int(raw_input('First day of week: '))
dayFriday = int(raw_input('Last day of week: '))
month = int(raw_input('Month: '))
year = 2016
projectname = '{0}.{2}.{3} - {1}.{2}.{3}'.format(dayMonday, dayFriday, month, year)
print(projectname)

if projectname:
  fullPath = os.path.join(path, projectname)
  createFolder(fullPath)


for f in folders:
  folder = os.path.join(fullPath, f)
  createFolder(folder)

