FROM node:20-alpine AS builder

WORKDIR /front_end

COPY package*.json ./

RUN npm install

COPY . ./

RUN npm run build

#COPY ./webserver/default.conf /etc/nginx/conf.d/default.conf
#COPY --from=build /frontend/build /usr/share/nginx/html
CMD cp -r build result_build
