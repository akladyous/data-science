# Grouping Data into Intervals

Determining the number of bins (intervals) in a histogram involves choosing a suitable division of
your data. Two commonly used approaches are the Square Root Rule and Sturges' Formula.

### 1. Square Root Rule:

- Calculate the square root of the total number of data points.
- Round up to the nearest whole number.

  - Number of Bins = Ceiling(Square Root of Total Number of Data Points)

- Example:
  - Number of Bins = Ceiling(Square Root of 100) = Ceiling(10) = 10

### 2. Sturges' Formula:

- Use Sturges' formula:

  - Number of Bins = 1 + Log base 2 (Total Number of Data Points)

- Example:
  - Number of Bins = 1 + Log base 2 (100) ≈ 1 + 6.64 ≈ 7.64
  - Round up to the nearest whole number: Ceiling(7.64) = 8

Remember, the optimal number of bins can vary. Experiment with different bin widths to visually
inspect the distribution and choose what makes sense for your dataset.

# Best Practices for Grouping Data into Intervals:

1. **Determine the Range:**

   - Calculate the range by subtracting the minimum from the maximum value.
   - Range = Maximum - Minimum

2. **Select the Number of Intervals (Bins):**

   - Choose a suitable number based on the nature and size of your data.
   - Number of Intervals = 5 to 20

3. **Calculate the Interval Width:**

   - Divide the range by the number of intervals.
   - Interval Width = Range / Number of Intervals

4. **Determine a Starting Point:**

   - Choose a starting point with more precision than the data.
   - Starting Point = Smallest Data Value - Small Value for Precision

5. **Create Class Limits:**

   - Use the starting point to create class limits for each interval.
   - Class Limits = Starting Point + Interval Width

6. **Calculate Class Midpoints:**

   - For each interval, calculate the class midpoint.
   - Class Midpoint = (Lower Class Limit + Upper Class Limit) / 2

7. **Ensure No Data Falls on Boundaries:**
   - Round class limits and midpoints appropriately.
