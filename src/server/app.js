const express = require('express')
const pg = require('pg')

const app = express()


function getGeneralCostBySubs(req, res) {
    res.end("ROUTE1")
}

function getGeneralCostByServices(req, res) {
    res.end("ROUTE2")
}

function getSubCostByService(req, res) {
    res.end("ROUTE3")
}

function getServicesCostBySub(req, res) {
    res.end("ROUTE4")
}

app.get("/api/cost/general/subscriptions", getGeneralCostBySubs)
app.get("/api/cost/general/services", getGeneralCostByServices)
app.get("/api/cost/services/:service", getServicesCostBySub)
app.get("/api/cost/subscriptions/:subscription", getSubCostByService)

app.listen(8080, () => {
    console.log("Listening on port 8080")
})
