#include "stdio.h"
#include "stdlib.h"
#include "string.h"

int main()
{

char saisie[50] = "";
printf("Entrez le mot de passe...: ");
scanf("%s",saisie);


if (strcmp(saisie,"MonSuperMotDePasse")==0)
{
printf("Mot de passe correct \n");

}
else
{
printf("Mot de passe incorrect \n");

}

return 0;
} 
