import librosa
from mutagen.mp3 import MP3
from helper_functions import *

def get_audio_vals(audio_path=None, polls_per_second=16):
    audio = MP3(audio_path)
    values, sample_rate = librosa.load(audio_path)
    audio_duration = int(audio.info.length)
    total_polls_wanted = audio_duration * polls_per_second
    averages = shorten_list_to_averages(values, total_polls_wanted)
    print(str(len(averages)) + " <-- actual vals in averages || expected total polls wanted ---> " + str(
        total_polls_wanted))
    print("averaged values - " + str(averages[0:10]))
    return averages

def plot(lst_vals: list):
    x = np.arange(len(lst_vals))
    plt.plot(x, lst_vals)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Array Visualization')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    averages = get_audio_vals(r"C:\Users\adity\Downloads\liftmefromtheground.mp3")
    plot(averages)
