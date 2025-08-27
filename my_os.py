import os

pwd = os.getcwd()
os.makedirs('test/test1', exist_ok=True)
os.chdir('{0}/test/test1'.format(pwd))
print(os.getcwd())
os.chdir(pwd)
os.removedirs('test/test1')
# print(os.listdir())
test = os.path.join(pwd, 'test.py')
print(test)
print(os.path.exists(test))
print(os.path.isdir(test))
print(os.path.isfile(test))
print(os.path.basename(test))
print(os.path.dirname(test))
print(os.path.split('/tmp/tmp1/tst.txt'))
print(os.path.splitext('/tmp/tmp1/tst.txt'))

print(os.environ['NUMBER_OF_PROCESSORS'])
for k, v in os.environ.items():
    print(k, v)

# for cdir, sdir, fils in os.walk(pwd):
#     print('cwd:', cdir)
#     print('sub:', sdir)
#     print('fil:', fils)
#     print('---')
