import psutil
import matplotlib.pyplot as plt

data = []

for i in range(28):
    value = psutil.cpu_percent(interval=0.2, percpu=True)
    print("psutil.cpu_percent = %s" % (value))
    data.append(value)

#plot
transposed_data = list(zip(*data))
for i, index_data in enumerate(transposed_data):
    plt.plot([x * 0.3 for x in range(1, len(data) + 1)], index_data, label=f'Core {i}')
plt.xlabel('Time (sec)')
plt.ylabel('Percentage (%)')
plt.title('CPU Utilization per core')
plt.legend()
plt.grid(True)
plt.show()

#table
for i, inner_list in enumerate(data):
    # Add the index as the first element of the inner list
    inner_list.insert(0, round((i+1)*0.2,1))

data.insert(0, ['instant', 'core0', 'core1', 'core2', 'core3', 'core4', 'core5', 'core6', 'core7'])

fig, ax = plt.subplots()
ax.axis('off')
table = ax.table(cellText=list(data), loc='center', cellLoc='center')
table.auto_set_column_width([0])  
table.auto_set_font_size(False)
table.set_fontsize(6)
table.scale(0.5, 1)
plt.show()