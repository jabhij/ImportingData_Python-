"""
Instructions --

- Assign the HDF5 group data['strain'] to group.
- In the for loop, print out the keys of the HDF5 group in group.
- Assign to the variable strain the values of the time series data data['strain']['Strain'] using the attribute .value.
- Set num_samples equal to 10000, the number of time points we wish to sample.
- Execute the rest of the code to produce a plot of the time series data in LIGO_data.hdf5.
"""

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

"""
PLOT 3
"""
