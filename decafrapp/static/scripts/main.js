const caffeineCtx = 'caffeineIntake'
const drinkCtx = 'drinkBreakdown'

fetch('http://localhost:8000/total_entries')
    .then(response => {
        return response.json()
    })
    .then(res => {
        const drinkEntries = res

        if (drinkEntries.length > 0) {
            document.getElementById('caffeineIntake').hidden = false
            const caffeineData = {
                labels: [],
                datasets: [{
                    label: 'Caffeine mg',
                    data: [],
                }]
            }
            drinkEntries.forEach(drinkEntry => {
                caffeineData.labels.push(drinkEntry.drink.name)
                caffeineData.datasets[0].data.push(drinkEntry.drink.caffeine_mg)
            });
            
            const options = {}
            const caffeineIntake = new Chart(caffeineCtx, {
                type: 'line',
                data: caffeineData,
                options: options
            })
        }


        // const drinkData = {
        //     labels: [],
        //     datasets: [{
        //         label: 'Drink types',
        //         data: []
        //     }]
        // }

        // let drinkTypes = []

        // drinkEntries.forEach(drinkEntry => {
            
        // });

        // const drinkBreakdown = new Chart(drinkCtx, {
        //     type: 'pie',
        //     data: drinkData
        // })
    })
