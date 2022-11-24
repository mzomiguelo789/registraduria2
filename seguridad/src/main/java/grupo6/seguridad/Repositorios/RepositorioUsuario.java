package grupo6.seguridad.Repositorios;
import grupo6.seguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends MongoRepository<Usuario,String> {
    @Query("{'correo': ?0}")
    public Usuario getUsuarioByEmail(String correo);
}
