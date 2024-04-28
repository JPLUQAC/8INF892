# Partcipants 060 - Conduire

## Instruction

```
You are an expert on analyzing human activities based on IMU recordings.
```

# Tests

## Zero-shot 

### Prompt

``` 
The IMU data is collected from a watch attached to the user‘s wrist with a sampling rate of 100Hz. The IMU data is given in the IMU coordinate frame. The three-axis accelerations are given below:
1. x-axis: [ -0.71 -0.82 -0.90 -0.85 -0.69 -0.60 -0.52 -0.49 -0.50 -0.55 -0.60 -0.61 -0.55 -0.46 -0.39 -0.25 -0.08 -0.25 -0.44 -0.50 -0.55 -0.72 -0.90 -0.93 -0.85 -0.66 -0.55 -0.49 -0.50 -0.50 -0.46 -0.49 -0.55 -0.57 -0.58 -0.64 -0.61 -0.55 -0.50 -0.52 -0.57 -0.53 -0.46 -0.44 -0.42 -0.38 -0.35 -0.38 -0.36 -0.42 -0.50 -0.49 -0.50 -0.49 -0.49 -0.58 -0.72 -0.74 -0.68 -0.63 -0.63 -0.60 -0.49 -0.46 -0.57 -0.71 -0.72 -0.75 -0.74 -0.75 -0.69 -0.71 -0.68 -0.58 -0.55 -0.53 -0.64 -0.66 -0.58 -0.50 -0.53 -0.52 -0.44 -0.33 -0.25 -0.31 -0.42 -0.52 -0.53 -0.49 -0.49 -0.49 -0.46 -0.47 -0.53 -0.61 -0.63 -0.53 -0.41 -0.33 -0.35 -0.36 -0.39 -0.36 -0.44 -0.53 -0.52 -0.44 -0.38 -0.39 -0.41 -0.35 -0.23 -0.25 -0.31 -0.36 -0.38 -0.39 -0.39 -0.39 -0.93 -0.30 -0.19 -0.08 -0.12 -0.44 -0.42 -0.61 -0.33 -0.44 -0.23 -0.25 -0.42 -0.08 -0.09 -0.35 -0.22 -0.31 -0.22 -0.23 -0.31 -0.44 -0.36 -0.39 -0.30 -0.20 -0.22 -0.14 -0.16 -0.19 -0.31 -0.33 -0.33 -0.27 -0.03 0.06 0.13 0.02 -0.09 -0.28 -0.23 -0.53 -0.33 0.14 0.36 0.30 0.38 0.16 -0.12 -0.22 -0.22 -0.22 -0.17 -0.17 -0.16 -0.14 -0.08 -0.09 -0.14 -0.22 -0.28 -0.35 -0.41 -0.44 -0.46 -0.46 -0.42 -0.36 -0.23 -0.27 -0.39 -0.41 -0.47 -0.53 -0.52 -0.46 -0.42 -0.30 -0.23 -0.38 ]
2. y-axis: [ 0.41 0.43 0.41 0.40 0.38 0.38 0.38 0.41 0.43 0.43 0.43 0.43 0.43 0.43 0.41 0.40 0.40 0.41 0.43 0.45 0.46 0.48 0.49 0.46 0.43 0.41 0.43 0.45 0.45 0.41 0.37 0.37 0.40 0.43 0.45 0.41 0.40 0.38 0.38 0.40 0.41 0.43 0.43 0.41 0.40 0.41 0.46 0.48 0.45 0.43 0.41 0.38 0.38 0.40 0.40 0.38 0.37 0.35 0.34 0.37 0.40 0.38 0.35 0.32 0.34 0.34 0.30 0.29 0.30 0.29 0.27 0.27 0.26 0.29 0.30 0.35 0.35 0.32 0.35 0.37 0.35 0.34 0.32 0.35 0.37 0.35 0.35 0.37 0.38 0.38 0.35 0.35 0.32 0.30 0.27 0.27 0.29 0.35 0.37 0.35 0.32 0.30 0.29 0.27 0.24 0.21 0.24 0.26 0.26 0.21 0.18 0.18 0.23 0.27 0.30 0.30 0.29 0.24 0.20 0.13 0.02 0.01 0.16 0.21 0.29 0.43 0.56 0.63 0.56 0.43 0.35 0.26 0.15 0.16 0.18 0.18 0.24 0.29 0.35 0.40 0.40 0.40 0.38 0.34 0.31 0.34 0.34 0.37 0.38 0.40 0.42 0.40 0.45 0.48 0.54 0.60 0.57 0.53 0.49 0.42 0.37 0.40 0.45 0.60 0.93 1.23 1.50 1.28 0.78 0.42 0.29 0.27 0.29 0.37 0.40 0.43 0.45 0.49 0.49 0.49 0.51 0.51 0.51 0.49 0.48 0.45 0.38 0.35 0.32 0.31 0.32 0.38 0.42 0.38 0.38 0.42 0.40 0.43 0.53 0.43 ]
3. z-axis: [ 0.65 0.69 0.76 0.76 0.76 0.69 0.60 0.57 0.56 0.57 0.65 0.69 0.71 0.74 0.66 0.52 0.46 0.56 0.54 0.52 0.48 0.45 0.51 0.56 0.54 0.54 0.54 0.65 0.65 0.73 0.79 0.73 0.68 0.65 0.66 0.73 0.74 0.68 0.63 0.63 0.63 0.57 0.57 0.62 0.63 0.59 0.60 0.62 0.57 0.62 0.73 0.69 0.63 0.65 0.66 0.71 0.74 0.76 0.74 0.68 0.66 0.66 0.66 0.57 0.57 0.65 0.71 0.73 0.74 0.77 0.77 0.87 0.83 0.76 0.71 0.68 0.71 0.65 0.65 0.65 0.68 0.76 0.74 0.71 0.68 0.71 0.74 0.77 0.74 0.73 0.68 0.68 0.69 0.74 0.77 0.82 0.88 0.88 0.79 0.74 0.69 0.74 0.71 0.63 0.69 0.76 0.76 0.76 0.69 0.73 0.79 0.82 0.71 0.71 0.68 0.73 0.73 0.76 0.76 0.77 1.35 0.87 0.57 0.57 0.60 0.65 0.76 0.76 0.76 0.99 0.93 0.99 1.11 0.90 0.83 0.99 0.79 0.82 0.71 0.76 0.79 0.93 0.90 0.93 0.90 0.76 0.76 0.68 0.70 0.73 0.79 0.73 0.80 0.65 0.48 0.57 0.70 0.74 0.79 0.91 0.79 1.16 0.63 -0.08 0.18 0.21 0.34 0.83 0.99 1.11 0.97 0.87 0.76 0.76 0.76 0.74 0.73 0.76 0.79 0.77 0.76 0.79 0.83 0.85 0.90 0.94 0.96 0.96 0.93 0.87 0.83 0.83 0.93 0.88 0.74 0.73 0.66 0.49 0.66 0.70 ]
The person's action belongs to one of the following categories: [driving, sleep, eating, walking].
Could you please tell what action the person was doing based on the given information and IMU readings? Please make an analysis step by step. 
```

### Réponse

``` 

```

## Zero-shot avec retrait de certaines données

### Prompt

``` 
The IMU data is collected from a watch attached to the user‘s wrist with a sampling rate of 100Hz. The IMU data is given in the IMU coordinate frame. The three-axis accelerations are given below:
1. x-axis: []
2. y-axis: []
3. z-axis: []
The person's action belongs to one of the following categories: [driving, sleep, eating, walking].
Could you please tell what action the person was doing based on the given information and IMU readings? Please make an analysis step by step.
```

### Réponse

``` 

```

## Explication des données brutes

### Prompt

``` 
The following IMU data is collected from an undisclosed sensor on a human participant. The three-axis of the data are given below:
1. x-axis: []
2. y-axis: []
3. z-axis: []
Could you please interpret the given IMU readings and tell what type of sensor it is coming from, what type of data it is and what it could represent? Please make an analysis step by step.
```

### Réponse

``` 

```