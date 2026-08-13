# Temperature Converter Pro

## Project Overview

Temperature Converter Pro is a premium, real-time web application designed to accurately convert temperature values between various scientific and standard scales. Built with a highly professional, modern UI, it feels like a production-ready utility.

## OIBSIP Task

**Web Development Level 1 — Task 3: Temperature Converter Website**

## Objective

The objective of this project is to build a professional temperature conversion application that allows users to easily input values, select their starting unit, and instantly see accurately calculated conversions. The tool is designed to be mathematically robust, strictly enforcing scientific rules like absolute zero limits, while providing a flawless user experience across all devices.

## Technologies Used

- **HTML5**: Semantic structure and accessible layout.
- **CSS3**: Premium visual styling, responsive design (Flexbox & Grid), and custom UI interactions.
- **Vanilla JavaScript**: DOM manipulation, mathematical formulas, and real-time input validation.
- *(No external libraries or frameworks like React, Tailwind, or Bootstrap were used, keeping the project lightweight and native)*

## Features

- **Real-time Conversion**: Calculates and updates values flawlessly.
- **Dynamic Result Cards**: Cleanly highlights active and converted values.
- **Input Validation**: Rejects empty fields or non-numeric characters.
- **Absolute-Zero Protection**: Strictly blocks scientifically impossible temperature values.
- **Quick Reference Table**: Common temperature milestones (freezing, room temp, boiling) at a glance.
- **Reset Functionality**: Instantly clears the application back to its default state.

## Supported Units

- **Celsius (°C)**
- **Fahrenheit (°F)**
- **Kelvin (K)**

## Conversion Logic

The underlying mathematical models used for conversion are strictly standard:

- **Celsius → Fahrenheit**: `(C × 9/5) + 32`
- **Celsius → Kelvin**: `C + 273.15`
- **Fahrenheit → Celsius**: `(F - 32) × 5/9`
- **Fahrenheit → Kelvin**: `(F - 32) × 5/9 + 273.15`
- **Kelvin → Celsius**: `K - 273.15`
- **Kelvin → Fahrenheit**: `(K - 273.15) × 9/5 + 32`

*All output results are cleanly rounded to 2 decimal places.*

## Validation

- **Numeric Checks**: Evaluates standard input formats and blocks submission of text/NaN.
- **Absolute Zero Protection**: 
  - Celsius cannot be below **-273.15°C**
  - Fahrenheit cannot be below **-459.67°F**
  - Kelvin cannot be below **0 K**
  - If a user attempts to convert these, a visible error state is presented preventing the mathematical operation.

## Responsive Design

The application utilizes fluid layouts and targeted CSS media queries to scale seamlessly across viewports:
- Desktop (1440px / 1280px / 1024px)
- Tablet (768px)
- Mobile (430px / 390px / 375px)

## Project Structure

```text
WebDev-L1-TempCon/
│
├── index.html        # Main HTML layout
├── style.css         # Styling and responsive rules
├── script.js         # Core validation and conversion logic
├── README.md         # Documentation
│
└── screenshots/      # Directory containing visual testing evidence
    ├── 01-home.png
    ├── 02-converter-empty-state.png
    ├── 03-valid-celsius-conversion.png
    ├── 04-valid-fahrenheit-conversion.png
    ├── 05-valid-kelvin-conversion.png
    ├── 06-invalid-input.png
    ├── 07-absolute-zero-error.png
    ├── 08-quick-reference.png
    ├── 09-how-it-works.png
    ├── 10-features.png
    ├── 11-footer.png
    ├── 12-mobile-responsive.png
    └── 13-full-page.png
```

## How to Run

1. Clone or download the repository to your local machine.
2. Navigate to the `WebDev-L1-TempCon` folder.
3. Open `index.html` in any modern web browser (Chrome, Firefox, Safari, Edge).
4. No build steps or server setup is strictly required; the application runs locally.

## OIBSIP Checklist

- [x] Numeric input
- [x] Input validation
- [x] Celsius/Fahrenheit/Kelvin selector
- [x] Output for all units
- [x] Convert button
- [x] Result display
- [x] Absolute-zero validation
- [x] Clean centered UI
- [x] Responsive design
