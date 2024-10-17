for (const i of [1, 2, 3, 4, 5, 6]) {
    document.getElementById("slider" + i).addEventListener('change', function (event) {
        const qs = new URLSearchParams({
            vo2max: document.getElementById("slider1").value,
            vlamax: document.getElementById("slider2").value,
            bw: document.getElementById("slider3").value,
            ks1: document.getElementById("slider4").value,
            ks2: document.getElementById("slider5").value,
            volrel: document.getElementById("slider6").value,
        })

        result = fetch(`http://127.0.0.1:5000/`, {
            method: "POST",
            body: qs
        })
            .then((response) => response.json())
            .then(data => {
                document.getElementById("carb-max").innerHTML = data["CarbMax"];
                    document.getElementById("lactate").innerHTML = data["Lactate"];
                       document.getElementById("t-pred").innerHTML = data["Predicted Time"];
                document.getElementById("at-speed").innerHTML = data["AT"];
                    document.getElementById("at-percent").innerHTML = data["Percantage of VO2max"];
                        document.getElementById("fat-max").innerHTML = data["FatMax"];
                document.getElementById("plot-pic").src = "../static/plots/plot.png?t=" + new Date().getTime();


            })
    })
}
function generatePDF() {
    const { jsPDF } = window.jspdf;
    const pdf = new jsPDF();
    // Set modern font and style
    pdf.setFont("Helvetica", "normal");
    pdf.setFontSize(12);
    // Plot image source
    const plotImageSrc = document.getElementById('plot-pic').src;
    // Box 1 slider values
    const box1Values = {
        vo2Max: document.getElementById('slider1').value,
        vLamax: document.getElementById('slider2').value,
        bodyWeight: document.getElementById('slider3').value,
        ks1: document.getElementById('slider4').value,
        ks2: document.getElementById('slider5').value,
        volRel: document.getElementById('slider6').value
    };
    // Box 1 labels and units
    const box1Labels = [
        'VO2max',
        'vLamax',
        'Body Weight',
        'Ks1',
        'Ks2',
        'VolRel'
    ];
    const box1units = [
        'ml/kg/min',
        'mmol/l',
        'kg',
        '',
        '',
        '%'
    ];
    // Box 2 values (computed from Flask)
    const box2Values = {
        carbMax: document.getElementById('carb-max').innerText,
        lactate: document.getElementById('lactate').innerText,
        tPred: document.getElementById('t-pred').innerText,
        atSpeed: document.getElementById('at-speed').innerText,
        atPercent: document.getElementById('at-percent').innerText,
        fatMax: document.getElementById('fat-max').innerText
    };
    // Box 2 labels and units
    const box2Labels = [
        'CarbMax',
        'Lactate Steady State',
        'Predicted Marathon Time',
        'AT Speed',
        'AT Percent',
        'FatMax'
    ];
    const box2units = [
        'm/s',
        'm/s',
        'h',
        'm/s',
        '% of VO2max',
        'm/s'
    ];
    // Add Box 1 slider values (above the plot) with modern styling
    pdf.setFont("Helvetica", "bold")
    pdf.setFontSize(16);
    pdf.text('Athlete Data:', 20, 20);
    pdf.setFont("Helvetica", "normal")
    pdf.setFontSize(12);
    pdf.setTextColor(60, 60, 60);
    let yPosition = 30;
    Object.keys(box1Values).forEach((key, index) => {
        pdf.text(`${box1Labels[index]}: ${box1Values[key]} ${box1units[index]}`, 20, yPosition);
        yPosition += 10;
    });
    // Load and add the plot image to the PDF
    const img = new Image();
    img.src = plotImageSrc;
    img.onload = function() {
        // Add the plot image
        yPosition += 10;
        pdf.addImage(img, 'PNG', 20, yPosition, 170, 100); // Adjust size as needed
        yPosition += 110;  // Adjust for plot height
        // Add Box 2 values (below the plot) with modern styling
        pdf.setFont("Helvetica", "bold")
        pdf.setFontSize(16);
        pdf.text('Performance Metrics:', 20, yPosition);
        pdf.setFont("Helvetica", "normal")
        pdf.setFontSize(12);
        pdf.setTextColor(60, 60, 60);
        yPosition += 10;
        Object.keys(box2Values).forEach((key, index) => {
            pdf.text(`${box2Labels[index]}: ${box2Values[key]} ${box2units[index]}`, 20, yPosition);
            yPosition += 10;
        });
        // Set final font style and download PDF
        pdf.setFont("Helvetica", "normal");
        pdf.setFontSize(10);
        pdf.setTextColor(100, 100, 100);
        pdf.text("Generated with ...", 20, yPosition + 20);
        // Save the PDF
        pdf.save("plot_with_values.pdf");
    };
}