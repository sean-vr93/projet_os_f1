// gcc -o go main.c -lpthread

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>

#define NUM_THREADS 20

double randomNumbers[NUM_THREADS];


// Function to generate a random number between 25 and 45 with 3 decimal places
double generateRandomNumber() {
    // Generate a random number between 0 and 1
    double random = (double)rand() / RAND_MAX;
    
    // Scale and shift the random number to be between 25 and 45 with 3 decimal places
    double result = 25 + random * (45 - 25);
    
    return result;
}

// Function to be executed by each thread
void* threadFunction(void* arg) {
    long thread_id = (long)arg;
    
    // Call the generateRandomNumber function and store the result in the global array
    randomNumbers[thread_id] = generateRandomNumber();
    
    pthread_exit(NULL);
}

// Function to create and run threads
void createAndRunThreads() {
    srand(time(NULL));

    // Create an array to hold thread IDs
    pthread_t threads[NUM_THREADS];

    // Create and run 20 threads
    for (long i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL, threadFunction, (void*)i);
    }

    // Wait for all threads to finish
    for (long i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }
}

int main() {
    // Call the function to create and run threads
    createAndRunThreads();
    
    // Print the random numbers stored in the global array
    for (long i = 0; i < NUM_THREADS; i++) {
        printf("Thread %ld: %.3lf\n", i, randomNumbers[i]);
    }

    return 0;
}
