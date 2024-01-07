# Challenge: Creating a Sorting Algorithm Visualisor Without GUI Experience - The Noob's Journey

## Why?
Wanted to test if I could create an app *Peacefully* using AI (ChatGPT, Bard, Bing) to gain insights about the future.

## How To Install
- Simply install the executable.
- Alternatively, download the repository, compile it yourself, and follow these steps:
    1. Unzip and enter the directory.
    2. Download Python 3.12.0.
    3. After installation, execute the following:
    ```bash
    python -m venv .venv
    .venv\Scripts\Activate
    pip uninstall pathlib
    pip install pyinstaller
    python -m pytinstaller gui.py
    ```

## App
### Description:
A straightforward app where you enter five numbers under ten in a text box. Submit it to check its correctness. Then select the algorithm type to execute and begin visualization.

### Gallery
For video: Navigate to the Media Files Folder.

## EXPERIENCE
### Approach
- Used existing Sorting Algorithms from GitHub (initially planned to use those provided by WilliamFiset).
- Attempted a Java-based module for GUI with moving bars displaying sorting algorithms.

#### What Happened
- **Bard's Guidance:** The journey commenced with Bard's advice, suggesting libraries that felt like a maze of complexity. Despite the uphill battle, delving into these libraries was a learning experience in itself, navigating through a sea of documentation and challenges.
    - _D3 Experiment:_ Initially, the D3 module seemed like the golden ticket, only to spring a surprise – it churned out a web app while I fervently craved a GUI. *The frustration was palpable!*
        - *Shift to Python:* With a heavy heart, I bid farewell to the Java to Python API concept, as the search yielded a disappointing outcome. *Cue dramatic sighs and a hint of exasperation.*
    - _New Approach:_ A glimmer of hope emerged as I stumbled upon a Python-based forked repo – a saving grace amidst the turbulent seas of trial and error.
    - **Module Trials:**
        1. **PyPlot:** The initial excitement was met with a shortfall in the animation department. *The disappointment was crushing.*
        2. **Altair:** Bard spoke highly of its SHIFT feature, but alas, it failed to harmonize with my animation aspirations. *A twist in the plot, yet again!*
        3. **Matplotlib & Turtle:** Playing the field between Matplotlib and Turtle, eventually, my heart was won over by Turtle's charm. Embracing Tkinter despite its tumultuous journey through errors and trials. *A rollercoaster ride of frustration and determination.*
            - _Tkinter-Turtle Drama:_ Attempting the integration was akin to an emotional rollercoaster, swinging between frustration and the occasional burst of laughter amidst the chaotic coding adventure. *Laughter, indeed, to cope with the challenging moments!*


### INSIGHTS Earned
- Relying solely on AI for app creation was tough; learning and self-planning are key.
- AI tools complement rather than replace developers; future needs might evolve.
- Better understanding of documentation before AI reliance saves time.
- AI utilization: Apply critical thinking and modify based on documentation understanding.

## IMP LINKS:-
1. [Python Algorithms](https://github.com/akzare/Algorithms)
2. [Executable file](https://github.com/SparshKhanna0001/Sorting-Data-Visualisor/blob/master/dist/gui/gui.exe)
