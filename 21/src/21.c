#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define n 3

struct Card {
  int init;
  char valeur[5];
  char couleur[7];
  int hash;
};

void play();
int checkWin(struct Card tab[]);
int valeurToInt(char *);
int addToTab(struct Card, struct Card tab[]);
void printChoice();
void cleanTab();
int isInDrop(struct Card, struct Card tab[]);
int hashCard(struct Card);
struct Card randCard();
void printCard(struct Card tab[]);
void printAll();

char *TAB_VALEUR[] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"};
char *TAB_COULEUR[] = {"Pique", "Carreau", "Coeur", "Trefle"};
struct Card TAB_DROP[n];
struct Card TAB_DROP_IA[n];

int main() {
  char ch;
  while (1) {
    printf("1. Start a game\n");
    printf("2. Rule\n");
    printf("3. Exit\n");
    scanf(" %c", &ch);
    switch (ch) {
      case '1':
        play();
        printf("\n\n\n\n\n\n");
        break;
      case '2':
        printf("Reach a final score higher than the dealer without exceeding 21; or let the dealer draw additional cards until their hand exceeds 21.\n");
        break;
      case '3':
        printf("Exiting Program\n");
        return 0;
      default:
        printf("You entered an invalid choice\n");
        break;
      }
  }
   return 0;
}

void play() {
  //init
  printf("Starting the game\n");
  cleanTab();
  addToTab(randCard(), TAB_DROP_IA);
  addToTab(randCard(), TAB_DROP);
  printAll();
  //user drop
  char playerMove;
  int iaMove;
  int limit = 0;
  while (1) {
    printf("\n\n");
    printf("1. Hit\n");
    printf("2. Stand\n");
    scanf(" %c", &playerMove);
    //PLAYER
    switch (playerMove) {
      case '1': //player drop a new card
        printf("You hit\n");
        addToTab(randCard(), TAB_DROP);
        break;
      case '2': //player do not drop a new card
        printf("You stand\n");
        break;
      default:
        printf("You entered an invalid choice\n");
        break;
      }
    //IA
    if ((checkWin(TAB_DROP_IA) <= 21 && (checkWin(TAB_DROP_IA) > (checkWin(TAB_DROP)))) && limit < 2) { //hit
        iaMove = 2;
    } else { //stand
        addToTab(randCard(), TAB_DROP_IA);
        iaMove = 1;
    }
    //AFFICHAGE
    printAll();
    //VERIFICATION
    if (checkWin(TAB_DROP) > 21) { //player lose
        printf("You Lose\n");
        return;
    } else if (checkWin(TAB_DROP_IA) > 21) { //IA lose
        printf("You Win\n");
        return;
    }
    //IA and player Stand or the limit is max the biggest value win
    if ((playerMove == '2' && iaMove == 2) || limit == 1) {
        if (checkWin(TAB_DROP_IA) < checkWin(TAB_DROP)) {
            printf("You Win\n");
            return;
        } else {
            printf("You Lose\n");
            return;
        }
    }
    limit++;
  }
}

//Print the hand of the IA and the player.
void printAll() {
  printf("\n");
  printf("Your Hand\n");
  printCard(TAB_DROP);
  printf("Dealer Hand\n");
  printCard(TAB_DROP_IA);
}

//Return the somme of the card in the tab given in arg.
int checkWin(struct Card tab[]) {
  int win = 0;
  for (int i=0; i < n; i++) {
    if (tab[i].init == 1) {
      win += valeurToInt(tab[i].valeur);
    } else {
      return win;
    }
  } return win;
}

//Return the value of the card.
int valeurToInt(char valeur[]) {
  int i = 0;
  if ((strcmp(valeur, "Valet") == 0) ||
      (strcmp(valeur, "Dame") == 0) ||
      (strcmp(valeur, "Roi") == 0)) {
    i = 10;
  } else if (strcmp(valeur, "As") == 0) {
    i = 1;
  } else {
    sscanf(valeur, "%d", &i);
  }
  return i;
}

//Add a card in the list tab, return 1 if all is ok, 0 otherwise.
int addToTab(struct Card card, struct Card tab[]) {
  for (int i=0; i < n; i++) {
    if (tab[i].init == 0) {
      tab[i] = card;
      return 1;
    }
  }
  return 0;
}

//Print all the card in the list given in arg.
void printCard(struct Card tab[]) {
  for (int i=0; i < n; i++) {
    if (tab[i].init == 1) {
      printf("    %s %s\n", tab[i].valeur, tab[i].couleur);
    } else {
      break;
    }
  }
  printf("\n    Total:    %d\n\n",checkWin(tab));
}

//Clean the tab.
void cleanTab() {
  for (int i=0; i < n; i++) {
    struct Card ca;
    ca.init = 0;
    TAB_DROP[i] = ca, TAB_DROP_IA[i] = ca;
  }
}

//Return 1 if the card is in the list given in arg, 0 if not.
int isInDrop(struct Card card, struct Card tab[]) {
  for (int i=0; i < n; i++) {
    if (tab[i].init == 1 &&
        tab[i].hash == card.hash) {
      return 1;
    }
  }
  return 0;
}

//Generate a hash (the hash will be the same if the components are the same).
int hashCard(struct Card card) {
  int i = (int)card.valeur + (int)card.couleur[1];
  return i;
}

//Return a new random card that is not in the two list.
struct Card randCard() {
  struct Card card;
  card.init = 1;
  strcpy(card.valeur, TAB_VALEUR[rand()%13]); // 0 12
  strcpy(card.couleur, TAB_COULEUR[rand()%4]); // 0 3
  card.hash = hashCard(card);
  if (isInDrop(card, TAB_DROP) == 0 && isInDrop(card, TAB_DROP_IA) == 0) {
    return card;
  } else {
    return randCard();
  }
}
