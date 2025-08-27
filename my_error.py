try:
    print('inside try')
    f = open('sample.json')
    print('inside try2')
except FileNotFoundError as e:
    print('inside FileNotFoundError')
    print(e)
except Exception as e:
    print('inside Exception')
    print(e)
else:
    print('inside else')
    data = f.read()
    f.close()
    print(type(data))
    print(len(data))
    print(data)
# finally:
#     print('inside finally')
