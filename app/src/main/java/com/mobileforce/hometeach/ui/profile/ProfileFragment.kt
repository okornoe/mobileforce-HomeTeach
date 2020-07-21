package com.mobileforce.hometeach.ui.profile

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.lifecycle.Observer
import androidx.navigation.NavController
import androidx.navigation.Navigation
import androidx.navigation.fragment.findNavController
import com.mobileforce.hometeach.R
import com.mobileforce.hometeach.databinding.FragmentProfileBinding
import com.mobileforce.hometeach.databinding.FragmentStudentProfileBinding
import com.mobileforce.hometeach.utils.AppConstants.USER_TUTOR
import com.mobileforce.hometeach.utils.PreferenceHelper
import com.mobileforce.hometeach.utils.Result
import com.mobileforce.hometeach.utils.snack
import org.koin.android.ext.android.inject
import org.koin.android.viewmodel.ext.android.viewModel

/**
 * Authored by enyason
 */
class ProfileFragment : Fragment() {
    private lateinit var bindingTutor: FragmentProfileBinding
    private val viewModel: ProfileViewModel by viewModel()
    private lateinit var bindingStudent: FragmentStudentProfileBinding
    private val pref: PreferenceHelper by inject()
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return if (pref.userType == USER_TUTOR){
            bindingTutor = FragmentProfileBinding.inflate(layoutInflater)
            bindingTutor.root
        }else{
            bindingStudent = FragmentStudentProfileBinding.inflate(layoutInflater)
            bindingStudent.root
        }


    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        if (pref.userType == USER_TUTOR) {
            setUpProfileForTutor()

        }else{
            setUpProfileForUser()
        }


    }
    private fun setUpProfileForTutor(){
        bindingTutor.editButton.setOnClickListener {
            findNavController().navigate(R.id.action_profileFragment_to_editTutorProfileFragment)
        }
        viewModel.getTutorDetails()
        viewModel.getTutorDetails.observe(viewLifecycleOwner, Observer { result ->
            Log.d("Result", result.toString())
            when (result) {
                Result.Loading -> {

                }
                is Result.Success -> {
                    bindingTutor.tutorName.text = result.data?.full_name
                    bindingTutor.tutorNameProfile.text= result.data?.full_name
                }

                is Result.Error -> {

                    bindingTutor.profileLayout.snack(message = result.exception.localizedMessage)
                }
            }

        })
        bindingTutor.viewAll.setOnClickListener {
            val mDialog = CredentialDialog.newInstance()
            mDialog.show(requireActivity().supportFragmentManager, "credentials")

        }
    }

    private fun setUpProfileForUser(){
        viewModel.getUserProfile()
        viewModel.getStudentProfile.observe(viewLifecycleOwner, Observer { result ->
            Log.d("Result", result.toString())
            when (result) {
                Result.Loading -> {

                }
                is Result.Success -> {
                    bindingStudent.ProfileName.text = result.data?.user?.fullName
                    bindingStudent.studentName.text = result.data?.user?.fullName
                    bindingStudent.descriptionText.text = result.data?.desc
                    bindingStudent.profileEmail.text = result.data?.user?.email
                    bindingStudent.profileNumber.text = result.data?.user?.phoneNumber
                }

                is Result.Error -> {

                    bindingStudent.studentProfileLayout.snack(message = result.exception.localizedMessage)
                }
            }

        })

    }

}