# Oral-Homework-Asking-AI

A Python-based interactive program that asks historical questions about Indian dynasties and expects spoken answers through a microphone. This tool helps users test their knowledge by verbally responding to questions in an engaging and personalized manner.

## Features

- **Historical Quiz**: Asks questions about various dynasties in India, including Rajput, Turkish Rulers, Khalji, Tughlaq, Sayyid, and Lodhi dynasties.
- **Customizable Data**: Users can add or modify historical data in a predefined object structure, allowing personalized quizzes.
- **Voice Interaction**: The program speaks the questions aloud and captures answers via the microphone, offering a unique oral practice experience.
  
## Getting Started

### Prerequisites
- Python 3.x
- Microphone for voice input
- Python packages (listed in `requirements.txt`)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Rahul-gif-asus/Oral-Homework-Asking-AI.git
   cd Oral-Homework-Asking-AI
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the program:
   ```bash
   python Main.py
   ```

2. Follow the instructions to answer the questions verbally when prompted.

3. **Customizing Data**:
   - You can modify the `DynastyMapping` object in `Main.py` to add your own dynasties and details.
   - Keep the variable structure intact to avoid errors in processing.

   ```python
   DynastyMapping = {
       "Rajput": {
           "Tomaras": "Early twelfth century to 1165",
           "Ananga Pala": "1130 to 1145",
           ...
       },
       ...
   }
   ```

## Example

Here’s a sample structure of the `DynastyMapping` object, which you can expand or edit:

```python
DynastyMapping = {
    "Rajput": {
        "Tomaras": "Early twelfth century to 1165",
        "Prithviraj Chauhan": "1175 to 1192",
    },
    "Khalji": {
        "Alauddin Khalji": "1296 to 1316",
    }
    ...
}
```

## Contributing

Feel free to fork this repository and make modifications. Pull requests are welcome!
