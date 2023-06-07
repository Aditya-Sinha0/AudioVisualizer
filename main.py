import librosa
from mutagen.mp3 import MP3
from helper_functions import *


audio_path = r"C:\Users\adity\Downloads\liftmefromtheground.mp3"
audio = MP3(audio_path)
values, sample_rate = librosa.load(audio_path)


audio_duration = int(audio.info.length)
total_samples = len(values)
#default polling rate is every 0.25 secs. add variable input later. make sure to account for more polls than samples
polls_per_second = 4
total_polls_wanted = audio_duration*polls_per_second
samples_per_poll = int(total_samples/total_polls_wanted)



#averages = [sum(group) / len(group) for group in zip(*[iter(values)] * samples_per_poll)]
averages = shorten_list_to_averages(values, total_polls_wanted)
print(str(len(averages)) + " <-- actual vals in averages || expected total polls wanted ---> " + str(total_polls_wanted))
print("averaged values - " + str(averages[0:10]))

x = np.arange(len(averages))
plt.plot(x, averages)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Array Visualization')
plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm is running')

