import re

ip_reg = re.compile(r'^d{1,3}.d{1,3}.d{1,3}.d{1,3}$')   
    
def main():
    inp = input('Insira o endereço IP: ')
    
    if inp == ip_reg:
        print('verdade')
    else:
        print('falso')
        
if __name__ == '__main__':
    main()

    