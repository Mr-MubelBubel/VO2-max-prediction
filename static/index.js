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
                document.getElementById("carb-max").innerHTML = data["CarbMax"],
                    document.getElementById("lactate").innerHTML = data["Lactate"],
                       document.getElementById("t-pred").innerHTML = data["Predicted Time"],
                document.getElementById("at-speed").innerHTML = data["AT"],
                    document.getElementById("at-percent").innerHTML = data["Percantage of VO2max"],
                        document.getElementById("fat-max").innerHTML = data["FatMax"]
            })
    })
}
