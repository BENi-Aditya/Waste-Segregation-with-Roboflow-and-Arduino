# Waste Segregation with Roboflow and Arduino

Waste Segregation with Roboflow and Arduino is a creative solution that uses computer vision and machine learning to identify and sort recyclable plastics, automating the recycling process. This project uses Roboflow's pre-trained model to categorize various plastics and uses Arduino to operate a servo motor for automated sorting. This technology helps to decrease human sorting labor and increase recycling rates, meeting the growing demand for effective waste management and recycling.


## Technologies Used

- **Roboflow**: For the pre-trained model to detect recyclable plastics.
- **OpenCV**: For video capture and frame processing.
- **Python**: Programming language used for backend development.
- **PySerial**: Library for serial communication with Arduino.
- **Arduino**: For controlling the servo motor based on detection results.

## Concept and Need

Recycling is a crucial process in waste management, aimed at reducing waste, conserving natural resources, and minimizing environmental impact. Manual sorting of recyclable materials is labor-intensive, time-consuming, and prone to human error. Automating this process with technology can significantly enhance efficiency and accuracy.

**Waste Segregation with Roboflow and Arduino** offers a smart solution to this problem. By using computer vision and machine learning, it accurately identifies various types of recyclable plastics. The integration with Arduino allows for precise control of the sorting mechanism, making the recycling process faster and more reliable.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Waste-Segregation-Roboflow-Arduino.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Waste-Segregation-Roboflow-Arduino
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory and add your API keys:**

    ```plaintext
    ROBOFLOW_API_KEY=your_roboflow_api_key_here
    ```

5. **Connect your Arduino and upload the appropriate sketch to it.**

6. **Run the script:**

    ```bash
    python inference_arduino.py
    ```

## Usage

- The script initializes the camera and continuously captures video frames.
- Type `s` in the terminal to send the current frame to Roboflow for inference.
- The detected plastic type will determine the command sent to the Arduino to sort the plastic.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or new features to add, feel free to open an issue or create a pull request.

---

<div align="center">
  <h2>Waste Segregation with Roboflow and Arduino - Automate Your Recycling</h2>
  <p>Identify and sort recyclable plastics efficiently using computer vision and machine learning.</p>
</div>
