# Instructor Notes

## Introduction

* Deliberate program design
* Testing
* Debugging
* Performance
* Packaging

## Part 1: Writing the Analysis Code

* Design patterns for our code
  * Restate our objective
  * What functions are necessary to go from our raw dataset to what we want?
  * Collaborative exercise to come up with a few design ideas
* Exercise: Reading a file
  * Write code
  * Return a list of dictionaries (one per row)
  * Tests to confirm that the code is working
* Concept of testing
  * Systematic way to ensure your code is working as expected
  * Different kinds of tests: unit, integration, ...
  * `if` statements, `assert` statements
  * Pre-written test that can be used with a small sample dataset to verify code
  * Have students run pre-written test
* Test-Driven Development
  * Given that we want to aggregate on test inspection data by `risk_category`,
    what tests would we need?
  * Exercise: Write own test data or use a fixture (TBD)
  * Run tests before the code exists (import error)
  * Show example tests and how we would run them
* Exercise: Write function and confirm that it matches the test
* Exercise: Repeat for all necessary functions
  * Aggregation code
* Exercise: putting all the functions together
* TBD: Include pdb

## Part 2: CLI

* Make the code into a command line script

## Part 3: Performance

* TBD: Performance profiling
  * snakeviz
  * pstats

## Part 4: Packaging
* Packaging
