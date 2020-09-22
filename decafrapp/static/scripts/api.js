const getData = () => {
    const address = 'http://localhost:8000'
    fetch(`${address}/total_entries`)
        .then(response => {
            return response.json()
        }).then(res => {
            return res
        })
    }
    
export { getData }