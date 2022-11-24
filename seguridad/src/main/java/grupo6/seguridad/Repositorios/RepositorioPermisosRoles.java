package grupo6.seguridad.Repositorios;
import org.springframework.data.mongodb.repository.MongoRepository;
import grupo6.seguridad.Modelos.PermisosRoles;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles, String>{
    @Query("{'rol.$id': ObjectId(?0),'permiso.$id': ObjectId(?1)}")
    PermisosRoles getPermisoRol(String id_rol,String id_permiso);
}
