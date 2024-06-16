// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <cs50.h>
#include <string.h>
#include "dictionary.h"
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>
// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;
int yolo = 0;
// TODO: Choose number of buckets in hash table
const unsigned int N = 150001;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
     // TODO

     node *boo = table[hash(word)];
     while(boo != NULL)
     {
        if(strcasecmp(word, boo->word) == 0)
        {
            return true;
            }
        else {boo = boo->next;}
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{

    int hash = 0;
    int kek = 0;
    for (int i = 0; i < strlen(word); i++)
    {
         hash = (hash << 5) + hash + word[i];

    }
    kek = hash/N + hash%N;

    if (kek >= N)
    {
        return hash%N;
    }

    return kek ;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *lol = fopen(dictionary, "r");
    if(lol == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];
     while (fscanf(lol, "%s", buffer) != EOF)
     {
        node *n = malloc(sizeof(node));
        if(n == NULL)
        {
            return false;
            }
            yolo++;
            strcpy(n->word, buffer);
         int x = hash(buffer);
             n->next = table[x];
            table[x] = n;
              }fclose(lol);
        return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return yolo;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i =0;i < N ;i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
        }
    }
    return true;
}
