package com.mobileforce.hometeach.data

import androidx.lifecycle.LiveData
import com.mobileforce.hometeach.data.model.User
import com.mobileforce.hometeach.data.repo.UserRepository
import com.mobileforce.hometeach.data.sources.DataSourceFactory
import com.mobileforce.hometeach.localsource.model.UserEntity
import com.mobileforce.hometeach.remotesource.Params
import com.mobileforce.hometeach.remotesource.wrappers.*
import retrofit2.Response


class UserRepositoryImpl(private val dataSource: DataSourceFactory) : UserRepository {

    override suspend fun login(params: Params.SignIn): Response<List<Any>> {
        return dataSource.remote().logIn(params)
    }

    override suspend fun register(params: Params.SignUp): RegisterUserResponse {
        return dataSource.remote().signUp(params)
    }

    override suspend fun saveUser(user: User) {
        dataSource.local().saveUser(user)
    }

    override suspend fun logOut() {
        dataSource.local().clearDb()
    }

    override suspend fun editTutorProfile(
        id: Int,
        params: Params.EditTutorProfile
    ): EditTutorProfileResponse {
        return dataSource.remote().editTutorProfile(id, params)
    }

    override suspend fun getProfileList(): List<ProfileResponse> {
        return dataSource.remote().getProfileList()
    }

    override suspend fun getTutorDetails(): TutorDetailsResponse {
        val user = dataSource.local().getSingleUser()
        return dataSource.remote().getTutorDetails(user.id.toDouble().toInt())
    }
    override fun getUser(): LiveData<UserEntity> {
        return dataSource.local().getUser()
    }

    override suspend fun password_reset(params: Params.PasswordReset): EmailResponse {
        return dataSource.remote().resetPassword(params)
    }



}