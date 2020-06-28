#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 1- Fonction init_int_alea
void init_int_alea(int max, int * result){
	*result = rand() % max;
}

// 2- Fonction init_tab_alea
void init_tab_alea(int max, int taille, int ** result_tab){
	for (int i=0; i<taille; i++){
		init_int_alea(max, result_tab[i]);
	}
}

int main(){
	srand(time(NULL));
	// Test de la fonction init_int_alea
	printf("Test de la fonction init_int_alea\n");
	printf("Veuillez entrer la valeur du maximum : ");
	int max;
	scanf("%d", &max);
	int * result;
	result = (int *) malloc(sizeof(int));
	init_int_alea(max, result);
	printf("%d\n", *result);
	free(result);

	// Test de la fonction init_tab_alea
	printf("Test de la fonction init_tab_alea\n");
	printf("Veuillez entrer la valeur du maximum : ");
	int maximum;
	scanf("%d", &maximum);
	printf("Veuillez entrer la taille du tableau a générer : ");
	int taille;
	scanf("%d", &taille);
	int ** result_tab;
	result_tab = (int **) malloc(taille * sizeof(int *));
	
for (int i=0; i<taille; i++)*result_tab = (int *) malloc(sizeof(int));
	init_tab_alea(maximum, taille, result_tab);
	for (int i=0; i<taille; i++){
		printf("%d\n", *result_tab[i]);
	}

	return 0;
}



