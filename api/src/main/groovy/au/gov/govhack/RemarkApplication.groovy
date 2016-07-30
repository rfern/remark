package au.gov.govhack

import org.springframework.beans.factory.annotation.Value
import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import springfox.documentation.builders.ApiInfoBuilder
import springfox.documentation.service.ApiInfo
import springfox.documentation.service.Contact
import springfox.documentation.spi.DocumentationType
import springfox.documentation.spring.web.plugins.Docket
import springfox.documentation.swagger2.annotations.EnableSwagger2

import static springfox.documentation.builders.PathSelectors.regex

@EnableSwagger2
@SpringBootApplication
@Configuration
class RemarkApplication {

    static void main(String ... args) {
        SpringApplication.run(RemarkApplication, args);
    }

    @Bean
    public Docket newsApi() {
        return new Docket(DocumentationType.SWAGGER_2)
                .groupName("remark-api")
                .apiInfo(apiInfo())
                .select()
                .paths(regex("/api/.*"))
                .build();
    }

    @Value('${swagger.title}')
    private String title;

    @Value('${swagger.description}')
    private String description;

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title(title)
                .description(description)
                .license("Apache License Version 2.0")
        //.licenseUrl("https://somelicense")
                .version("1.0")
                .contact(getContact())
                .build();
    }

    @Value('${swagger.contact.name}')
    String name;

    @Value('${swagger.contact.url}')
    String url;

    @Value('${swagger.contact.email}')
    String email;

    private Contact getContact() {
        if (name == null) {
            return null;
        }
        return new Contact(name, url, email);
    }
}
