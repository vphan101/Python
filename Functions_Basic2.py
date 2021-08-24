while True:
    un = input(">>")
    try:
        when_to_stop  =abs(int(un))
    except KeyboardInterrupt:
            break
    except:
            print("Not a number")

    while when_to_stop >0:
        when_to_stop -=1
        print(when_to_stop)

