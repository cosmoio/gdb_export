#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


/**
 * A broken function that uses an inherently unsafe function strcpy (see man strcpy) to copy 
 * a value without length check to a fixed size buffer
 * 
 * If a string is inserted that is too large, we expect an outcome smth. like this:
 * 
 * [!] Inside broken_func: ZZZZZZZZZZZZZZZZZZZZZZZZZ
 *  *** stack smashing detected ***: <unknown> terminated
 * Aborted (core dumped)
 *
 **/
void broken_func(char *fuzz_string)
{
	char dst[20];
	strcpy(dst, fuzz_string);
    
    printf("[!] Inside broken_func: %s\n",dst);
}


/**
 * A little fuzzing function for broken_func that inserts increasing strings of a specific pattern:
 * A, BB, CCC, DDD, ..
 **/
void fuzz(int length)
{
	char *fuzz_string = NULL;
	int max_fuzz_length = length;

	for (int i = 0; i < max_fuzz_length; i++)
	{
		fuzz_string = (char *) realloc(fuzz_string, i+1*sizeof(char));
		fuzz_string[i] = '\0';
        for (int j = 0; j < i; j++)
		{
            fuzz_string[j] = 65+i%95;
        }
        printf("[*] Fuzz string: %d %s\n",i,fuzz_string);
        
        printf("[!] Testing broken_func\n");
        broken_func(fuzz_string);
	}
    free (fuzz_string);

}

int main(int argc, char **argv)
{
    printf("[!] A little test for GDB\n");
    int opt;
    long length = 10;
    
    if (argc < 2)
    {
        printf("Usage: min_fuzz -l 10\n");
        exit(EXIT_SUCCESS);
    }
    
    while ((opt = getopt (argc, argv, "l:")) != -1)
    {
        switch (opt)
        {
          case 'l':
                    printf ("Fuzz length: %s\n", optarg);                          
                    char *endp = NULL;
                    if (!optarg ||  ((length=strtol(optarg, &endp,10)),(endp && *endp)))
                    { 
                        printf("[!] Error: Invalid l option %s - expecting a number\n", optarg?optarg:"");
                        exit(EXIT_FAILURE);
                     };

                    break;
          default:
                    printf("Usage: min_fuzz -l 10\n");
                    exit(EXIT_SUCCESS);
        }
      }

	fuzz(length);
}
