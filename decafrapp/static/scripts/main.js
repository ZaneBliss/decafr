const caffeineCtx = 'caffeineIntake'
const drinkDayCtx = 'drinksPerDay'
const drinkTypeCtx = 'drinkBreakdown'

fetch('http://localhost:8000/total_entries')
    .then(response => {
        return response.json()
    })
    .then(res => {
        const drinkEntries = res

        if (drinkEntries.length > 0) {
            document.getElementById('caffeineIntake').hidden = false
            document.getElementById('drinksPerDay').hidden = false

            // Caffeine per entry chart
            const caffeinePerDay = {}

            const caffeineData = {
                labels: [],
                datasets: [{
                    label: 'Caffeine mg',
                    data: [],
                }]
            }

            drinkEntries.forEach(drinkEntry => {
                if (caffeinePerDay.hasOwnProperty(dayjs(drinkEntry.date).format('dddd'))) {
                    caffeinePerDay[dayjs(drinkEntry.date).format('dddd')]++
                } else {
                    caffeinePerDay[dayjs(drinkEntry.date).format('dddd')] = 1
                }
            });
            console.log(caffeinePerDay);
            
            drinkEntries.forEach(drinkEntry => {
                caffeineData.labels.push(drinkEntry.drink.name)
                caffeineData.datasets[0].data.push(drinkEntry.drink.caffeine_mg)
            });

            const caffeineIntake = new Chart(caffeineCtx, {
                type: 'line',
                data: caffeineData,
                // options: {
                //     responsive: false,
                //     maintainAspectRatio: false
                // }
            })

            // Number of drinks per day chart
            const drinkDayData = {
                labels: [],
                datasets: [{
                    label: 'Number of drinks',
                    data: []
                }]
            }
            let entriesPerDay = {}

            drinkEntries.forEach(drinkEntry => {
                if (entriesPerDay.hasOwnProperty(dayjs(drinkEntry.date).format('dddd'))) {
                    entriesPerDay[dayjs(drinkEntry.date).format('dddd')]++
                } else {
                    entriesPerDay[dayjs(drinkEntry.date).format('dddd')] = 1
                }
            });

            for (const property in entriesPerDay) {
                drinkDayData.labels.push(property)
                drinkDayData.datasets[0].data.push(entriesPerDay[property])
            }

            const drinksPerDay = new Chart(drinkDayCtx, {
                type: 'line',
                data: drinkDayData,
                options: {
                    // responsive: false,
                    // maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            })

            // Types of drinks
            const drinkTypeData = {
                labels: [],
                datasets: [{
                    label: 'Number of drinks consumed',
                    data: []
                }]
            }
            let drinkTypes = {}

            drinkEntries.forEach(drinkEntry => {
                if (drinkTypes.hasOwnProperty(drinkEntry.drink.name)) {
                    drinkTypes[drinkEntry.drink.name]++
                } else {
                    drinkTypes[drinkEntry.drink.name] = 1
                }
            });
            
            for (const property in drinkTypes) {
                drinkTypeData.labels.push(property)
                drinkTypeData.datasets[0].data.push(drinkTypes[property])
            }

            const drinkTypeDay = new Chart(drinkTypeCtx, {
                type: 'doughnut',
                data: drinkTypeData,
                // options: {
                //     responsive: false,
                //     maintainAspectRatio: false,
                // }
            })
        }
    })
