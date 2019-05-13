#include <unistd.h>
#include <string.h>
#include <stdio.h>

void main(){
    char c;
    int a=0;
    FILE *fin,*fout;
    fin = fopen("breast-cancer-wisconsin.data","r");
    fout = fopen("aa.data","w")
    while((c=fgetc(fin))!=EOF){
        if(c==','){
            if(a!=0){
                fputc(c,fout);
            }
            a++;
            if(a==9) a=0;
        }
    }
    fclose(fin);
    fclose(fout);
}



