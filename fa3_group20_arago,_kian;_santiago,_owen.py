# -*- coding: utf-8 -*-
"""FA3_GROUP20_ARAGO, KIAN; SANTIAGO, OWEN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EFf3txfWgCD3xdm_jNteH0ZazYG0V2hX

2.  A binary communication channel carries data as one of two sets of signals denoted by 0 and 1. Owing to noise, a transmitted 0 is sometimes received as a 1, and a transmitted 1 is sometimes received as a 0. For a given channel, it can be assumed that a transmitted 0 is correctly received with probability 0.95, and a transmitted 1 is correctly received with probability 0.75. Also, 70% of all messages are transmitted as a 0. If a signal is sent, determine the probability that:

(a) a 1 was received;
"""

P_T0 <- 0.7
P_T1 <- 0.3
P_R0_given_T0 <- 0.95
P_R1_given_T0 <- 1 - P_R0_given_T0
P_R1_given_T1 <- 0.75
P_R0_given_T1 <- 1 - P_R1_given_T1

P_R1 <- (P_R1_given_T0 * P_T0) + (P_R1_given_T1 * P_T1)
cat("(a) Probability that a 1 was received:", P_R1, "\n")

"""(b) a 1 was transmitted given than a 1 was received."""

P_T1_given_R1 <- (P_R1_given_T1 * P_T1) / P_R1
cat("(b) Probability that a 1 was transmitted given that a 1 was received:", P_T1_given_R1, "\n")

"""7.  There are three employees working at an IT company: Jane, Amy, and Ava, doing 10%, 30%, and 60% of the programming, respectively. 8% of Jane’s work, 5% of Amy’s work, and just 1% of Ava‘s work is in error. What is the overall percentage of error? If a program is found with an error, who is the most likely person to have written it?"""

work_done <- c(Jane = 0.10, Amy = 0.30, Ava = 0.60)
work_error <- c(Jane = 0.08, Amy = 0.05, Ava = 0.01)

error_contributions <- work_done * work_error
overall_percentage_error <- sum(error_contributions) * 100

cat("Overall percentage error:", overall_percentage_error, "%\n")

percentage_errors <- error_contributions * 100
names(percentage_errors) <- names(work_done)

cat("Percentage error per person:\n")
print(percentage_errors)

person_error <- error_contributions / sum(error_contributions)
person_responsible <- names(which.max(person_error))

cat("Person responsible for the error:", person_responsible, "\n")