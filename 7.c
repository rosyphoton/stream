#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct student
{
    long studentID;
    char studentName[10];
}STUDENT;

int Readfile(STUDENT stu[]);

int main()
{
    int n,i,j,s;
    char ch;
    int times[80];
    STUDENT stu[80];
    for (i = 0; i < 80; i++)
    {
        times[i] = 0;
    }
    n = Readfile(stu);
    srand(time(NULL));
    do
    {
        s = rand()%n+1;
        times[s-1]++;
        printf("%ld",stu[s-1].studentID);
        printf("%s\n",stu[s-1].studentName);
        printf("times:%d\n",times[s-1]);
        printf("Continue? Y|y or  N|n\n");
        scanf(" %c",&ch);
    } while((ch == 'Y') || (ch == 'y'));
    return 0;
}

int Readfile(STUDENT stu[])
{
    FILE *fp;
    int i;
    if ((fp = fopen("student.txt","r")) == NULL)
    {
        printf("Failure to open the file!\n");
        exit(0);
    }
    for (i = 0; !feof(fp); i++)
    {
        fscanf(fp, "%ld", &stu[i].studentID);
        fscanf(fp, "%s", stu[i].studentName);
    }
    fclose(fp);
    return i;
}
