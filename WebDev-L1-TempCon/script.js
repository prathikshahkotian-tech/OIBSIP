/**
 * Temperature Converter Pro - Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const form = document.getElementById('converter-form');
    const tempInput = document.getElementById('temp-input');
    const unitSelect = document.getElementById('unit-select');
    const resetBtn = document.getElementById('reset-btn');
    const resultsContainer = document.getElementById('results-container');
    const inputGroup = tempInput.closest('.input-group');
    const errorMessage = document.getElementById('input-error');

    // Absolute Zero Constants
    const ABS_ZERO = {
        celsius: -273.15,
        fahrenheit: -459.67,
        kelvin: 0
    };

    // Initialize Event Listeners
    form.addEventListener('submit', handleConvert);
    resetBtn.addEventListener('click', handleReset);
    
    // Optional: Clear errors on input
    tempInput.addEventListener('input', clearError);
    unitSelect.addEventListener('change', () => {
        clearError();
        // If there's already a valid input, update results dynamically
        if (tempInput.value.trim() !== '') {
            if (!resultsContainer.classList.contains('hidden')) {
                handleConvert(new Event('submit'));
            }
        }
    });

    /**
     * Handle the form submission (Convert button click)
     */
    function handleConvert(e) {
        e.preventDefault();
        
        const inputValue = tempInput.value.trim();
        const unit = unitSelect.value;
        
        // Validation 1: Empty input
        if (inputValue === '') {
            showError("Please enter a temperature value.");
            return;
        }

        // Validation 2: Numeric check
        const temp = parseFloat(inputValue);
        if (isNaN(temp)) {
            showError("Please enter a valid numeric temperature.");
            return;
        }

        // Validation 3: Absolute Zero violation
        if (temp < ABS_ZERO[unit]) {
            showError(`Temperature cannot be below absolute zero (${ABS_ZERO[unit]}${getUnitSymbol(unit)}).`);
            return;
        }

        // Proceed to Conversion
        clearError();
        const results = calculateConversions(temp, unit);
        renderResults(results, unit);
    }

    /**
     * Calculate all conversions based on input and unit
     */
    function calculateConversions(val, fromUnit) {
        let c, f, k;

        if (fromUnit === 'celsius') {
            c = val;
            f = (val * 9/5) + 32;
            k = val + 273.15;
        } else if (fromUnit === 'fahrenheit') {
            c = (val - 32) * 5/9;
            f = val;
            k = (val - 32) * 5/9 + 273.15;
        } else if (fromUnit === 'kelvin') {
            c = val - 273.15;
            f = (val - 273.15) * 9/5 + 32;
            k = val;
        }

        return {
            celsius: c,
            fahrenheit: f,
            kelvin: k
        };
    }

    /**
     * Render the result cards in the DOM
     */
    function renderResults(results, activeUnit) {
        // Clear previous results
        resultsContainer.innerHTML = '';

        // Define order and data
        const unitsData = [
            { id: 'celsius', label: 'Celsius', val: results.celsius, sym: '°C' },
            { id: 'fahrenheit', label: 'Fahrenheit', val: results.fahrenheit, sym: '°F' },
            { id: 'kelvin', label: 'Kelvin', val: results.kelvin, sym: 'K' }
        ];

        // Create cards
        unitsData.forEach(item => {
            const card = document.createElement('div');
            card.className = `result-card ${item.id === activeUnit ? 'active' : ''}`;
            
            // Format number to 2 decimal places professionally
            // Use Number() to avoid trailing zeros if not needed, e.g. 25.00 -> 25, but strictly keeping 2 decimals often looks more professional. Let's strictly use 2 decimals.
            const displayVal = item.val.toFixed(2);

            card.innerHTML = `
                <span class="result-label">${item.label}</span>
                <span class="result-value">${displayVal}</span>
                <span class="result-unit">${item.sym}</span>
            `;
            resultsContainer.appendChild(card);
        });

        // Show container
        resultsContainer.classList.remove('hidden');
    }

    /**
     * Display error state
     */
    function showError(msg) {
        errorMessage.textContent = msg;
        inputGroup.classList.add('has-error');
        resultsContainer.classList.add('hidden');
    }

    /**
     * Clear error state
     */
    function clearError() {
        errorMessage.textContent = '';
        inputGroup.classList.remove('has-error');
    }

    /**
     * Reset the form to initial state
     */
    function handleReset() {
        form.reset();
        clearError();
        unitSelect.value = 'celsius';
        resultsContainer.classList.add('hidden');
        resultsContainer.innerHTML = '';
        tempInput.focus();
    }

    /**
     * Helper to get unit symbol
     */
    function getUnitSymbol(unit) {
        if (unit === 'celsius') return '°C';
        if (unit === 'fahrenheit') return '°F';
        return ' K';
    }
});
