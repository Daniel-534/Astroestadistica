#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define TOTAL_CANDIDATES 5000
#define ENVELOPE_CONSTANT 2.5
#define OUTPUT_PATH "rejection_data.dat"

double target_density(double candidate_x) {
    return 30.0 * candidate_x * pow(1.0 - candidate_x, 4.0);
}

int main(void) {
    srand(42);
    FILE *data_stream = fopen(OUTPUT_PATH, "w");
    if (!data_stream) {
        return 1;
    }

    for (int iteration = 0; iteration < TOTAL_CANDIDATES; ++iteration) {
        double candidate_x = (double)rand() / RAND_MAX;
        double candidate_y = ((double)rand() / RAND_MAX) * ENVELOPE_CONSTANT;
        int acceptance_status = (candidate_y <= target_density(candidate_x)) ? 1 : 0;
        fprintf(data_stream, "%.6f %.6f %d\n", candidate_x, candidate_y, acceptance_status);
    }

    fclose(data_stream);
    return 0;
}
