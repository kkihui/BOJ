# include <stdio.h>

int main() 
{
    float credit,creditSum=0,numGrade,gradeSum=0;
    char subject[51],grade[3];

    for (int i=0;i<20;i++)
    {
        scanf("%s %f %s",subject,&credit,grade);
        if (grade[0] == 'A') numGrade = 4.0;
        else if (grade[0] == 'B') numGrade = 3.0;
        else if (grade[0] == 'C') numGrade = 2.0;
        else if (grade[0] == 'D') numGrade = 1.0;
        else
        {
            numGrade = 0.0;
            if (grade[0] == 'P') credit = 0;
        }

        if (grade[1] == '+') numGrade += 0.5;
        creditSum += credit;
        gradeSum += numGrade*credit;
    }
    
    printf("%f",gradeSum/creditSum);

    return 0;
}