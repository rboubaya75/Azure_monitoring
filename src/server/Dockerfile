FROM node

WORKDIR /app

COPY . .

EXPOSE 8080

RUN npm install express pg

CMD ["node", "app.js"]