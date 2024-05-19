import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import textwrap

# Your data
data = {
    'January': 'Defined the project idea and objectives and met with our supervisor',
    'February': 'Gathered data about our model for training',
    'March': 'Labelled the gathered dataset and made UI for our android app',
    'April': 'Built and trained our model using yolov5 algorithm',
    'May-June': 'Will work on thesis',
    'July': 'Will work on thesis',
    'August': 'Will make model for face and extract eyes to feed our custom trained yolov5 model',
    'September': 'Will work on thesis',
    'October-November': 'Will work on real-time detection, testing, and app integration'
}

# Convert month names to datetime objects
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_map = {name: i + 1 for i, name in enumerate(month_names)}

start_dates = []
for month in data.keys():
    if '-' in month:
        start_month, end_month = month.split('-')
        start_month_num = month_map[start_month]
    else:
        start_month_num = month_map[month]
    start_dates.append(datetime.date(2023, start_month_num, 1))

end_dates = start_dates[1:] + [datetime.date(2023, 12, 1)]

# Plot the Gantt chart
fig, ax = plt.subplots(figsize=(12, 5))
for i, (start, end, task) in enumerate(zip(start_dates, end_dates, data.values())):
    ax.barh(len(data) - 1 - i, end - start, left=start, height=0.5)
    wrapped_task = textwrap.fill(task, width=20)
    ax.text(start, len(data) - 1 - i, wrapped_task, va='center', ha='left', fontsize=8)

ax.set_yticks(range(len(data)))
ax.set_yticklabels(reversed(data.keys()))
ax.set_xlabel('Timeline')
ax.set_ylabel('Months')
ax.set_title('Gantt Chart')

# Format the date axis
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.tight_layout()
plt.show()
