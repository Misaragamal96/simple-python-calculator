def name():
    # إدخال اسم المستخدم والترحيب به
    names = input("Hi, can you enter your name? ").strip()
    print("Hi " + names)

def opertor():
    while True:
        try:
            # أخذ الإدخال من المستخدم للأرقام والمشغل
            nm1 = float(input("Enter number one: "))
            print("Choose an operator:")
            print("1 - [+]\n2 - [-]\n3 - [/]\n4 - [%]\n5 - [*]")
            op1 = int(input("Enter the operator number: "))
            nm2 = float(input("Enter number two: "))

            # العمليات الحسابية بناءً على اختيار المستخدم
            if op1 == 1:
                print("Result:", nm1 + nm2)
            elif op1 == 2:
                print("Result:", nm1 - nm2)
            elif op1 == 3:
                # التحقق من القسمة على صفر
                if nm2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print("Result:", nm1 / nm2)
            elif op1 == 4:
                print("Result:", nm1 % nm2)
            elif op1 == 5:
                print("Result:", nm1 * nm2)
            else:
                print("Invalid operator choice. Please try again.")
            
            # تحقق إذا أراد المستخدم إنهاء البرنامج
            non = input("If you want to exit the program, enter 'non': ").strip().lower()
            if non == "non":
                print("Exiting the program...")
                break  # إنهاء الحلقة والخروج من البرنامج

        except ValueError:
            # معالجة الأخطاء الناتجة عن إدخال غير رقمي
            print("Please enter valid numbers.")

# --------------------------------------------------------------------------------------------------------------#
# استدعاء الدوال
name()
opertor()
