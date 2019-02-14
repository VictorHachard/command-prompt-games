#include <stdio.h>
#include <stdlib.h>
#include <math.h>


	int MAX_PUISSANCE = 4;

	//HANDELER LISTERNER
	int place(char tab[7][6], int toPlace) {
		for (int col=0; col < 6; col++) {
			if (tab[toPlace][col] == ' ') {
				return col;
			}
		} return 0;
	}

	//Return 1 if the place is free, 0 if not.
	int canPlace(char tab[7][6], int toPlace) {
		if (tab[toPlace][6] == ' ') {
			return 1;
		} return 0;
	}

	//Clean the tab.
	void cleanTab(char tab[7][6]) {
		for (int col=0; col < 6; col++) {
			for (int line=0; line < 7; line++) {
				tab[line][col] = ' ';
			}
		}
	}

	//Return 0 if no one win, 1 if red win, 2 if green win.
	int checkWin(char tab[7][6], char green, char red) {
	    return 0;
		for (int col=0; col-MAX_PUISSANCE < 6; col++) {
			for (int line=0; line-MAX_PUISSANCE < 7; line++) {
                    int i = line;
                    int j = col;
				if ((tab[i][j] == green && tab[i+1][j] == green && tab[i+2][j] == green && tab[i+3][j] == green) ||
					(tab[i][j] == green && tab[i][j+1] == green && tab[i][j+2] == green && tab[i][j+3] == green)) {

					return 1;
				} else if ((tab[i][j] == red && tab[i+1][j] == red && tab[i+2][j] == red && tab[i+3][j] == red) ||
							(tab[i][j] == red && tab[i][j+1] == red && tab[i][j+2] == red && tab[i][j+3] == red)) {

					return 2;
				}
			}
		}

		return 0;
	}

	//Print the tab.
	void printTab(char tab[7][6]) {
		for (int col=0; col < 6; col++) {
			for (int line=0; line < 7; line++) {
				printf(" %c ", tab[line][col]);
			} printf("\n");
		} printf("\n");
	}

	int main(void) {
		char tab[7][6];
		cleanTab(tab);
		int number;
		char green = 'g';
		char red = 'r';
		char atThisMoment = green;
		printf("debut");
		while (checkWin(tab, green, red) == 0) {
			number = 0;
			printf("cest a truc de jouer %c :", atThisMoment);
			if (atThisMoment == green) {
							atThisMoment = red;
						} else if (atThisMoment == red) {
							atThisMoment = green;
						}
			scanf("%d", &number);
			if (canPlace(tab, number)) {
				tab[number][place(tab, number)] = atThisMoment;
			}
			if (checkWin(tab, green, red) != 0) {
                   printf("WIN");
			}
			printTab(tab);
		}
		return 0;
	}
