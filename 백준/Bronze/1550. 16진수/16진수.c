#include<stdio.h>
#include<math.h>

int main()
{
    char hexa[7]={0},temp;
    int decimal = 0, length=0;
    
    scanf("%s",&hexa);

    for (int i=5;i>=0;i--)
    {
        temp = hexa[i];
        if (temp != 0)
        {
            if (48 <= temp && temp <= 57) // case1. temp is number 0~9
            {
                decimal += (((int)temp)-48)*pow(16,length); // ASCII '0' is int (48)
                length += 1; 
            }
            else if (65<= temp && temp<=70) // case2. temp is chr A~F
            {
                decimal += (((int)temp)-55)*pow(16,length); // ASCII 'A' is int (65) so -55 for represent 10~15
                length += 1; 
            }
            
        }
    }
    printf("%d",decimal);

    // printf("hexa: %s\ndeci: %d",hexa,decimal); // for testing
    
    return 0;
}
