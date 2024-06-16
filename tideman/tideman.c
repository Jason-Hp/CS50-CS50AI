#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];
int boo =0;
int s =0;
int p=0;
int r=0;
int HELP = 0;
// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];
int No[1000];
// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool brom (int x);
int crap(int x);
int main(int argc, string argv[])
{


    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    int a=0;
    for (int i=0; i<candidate_count; i++)
{
 if (strcmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i;
            a++;
        }
}
if (a == 0)
{return false;}
else
{
return true;
}
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO
    for (int i = 0; i<candidate_count-1;i++)
    {

        for (int j = i+1; j< candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
int b =0;
for (int i = 0; i< candidate_count; i++)
    {

        for (int j = 0; j< candidate_count; j++)
        {
            if (preferences[i][j] - preferences[j][i] > 0 & i != j)
             {
            pairs[b].winner = i;
            pairs[b].loser = j;

            b++;
             }
        }
    }
    pair_count = b;
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
int c = 0;
pair lol;

for (int i=0;i<pair_count;i++)
{
    for (int j=i;j<pair_count;j++)
    {
        if (preferences[pairs[i].winner][pairs[i].loser] < preferences[pairs[j].winner][pairs[j].loser] & i != j)
        {
            lol = pairs[i];
            pairs[i] = pairs[j];
            pairs[j] = lol;
           }
    }
}

     return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
 // TODO

int c = 0;
for (int i=0;i<pair_count;i++)
{

printf("%i\n",i);
printf("loser of i%s\n",candidates[pairs[i].loser]);
printf("winner of i%s\n",candidates[pairs[i].winner]);
   HELP = i;
   if (brom (i) == true)
{
    locked[pairs[i].winner][pairs[i].loser] = true;

}
    printf("%i\n",boo);
    if (boo>0)
    {
        locked[pairs[i].winner][pairs[i].loser] = false;
    }
    if (locked[pairs[2].winner][pairs[2].loser] == true)
    {
        printf("pls\n");
    }
boo = 0;
}

return;
}

// Print the winner of the election
void print_winner(void)
{

}

bool brom (int x)
{
int c = 0;
for (int i = 0;i<pair_count;i++)
{
if(locked[pairs[i].winner][pairs[x].winner] == true)
{
    {
        if (pairs[HELP].loser == pairs[i].winner)
        {
             if(locked[pairs[i].winner][pairs[i].loser] == true & HELP>1)
                {printf("Ok\n");
                 c++;
                boo++;
                 return false;}
            else
            {
                printf("omgggg\n");
                return true;
            }

        }
        else
        brom(i);
    }
}
if (c>0)
{printf("PPPPLLLOOOLLPPPPPP\n");
return false;}
}


if (c>0)
{printf("noo\n");
return false;}
else
{printf("PPPPPPPPPP\n");
return true;}

}