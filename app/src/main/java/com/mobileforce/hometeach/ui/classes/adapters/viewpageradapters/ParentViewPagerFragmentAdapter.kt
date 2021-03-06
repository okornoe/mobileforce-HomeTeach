package com.mobileforce.hometeach.ui.classes.adapters.viewpageradapters

import androidx.fragment.app.Fragment
import androidx.viewpager2.adapter.FragmentStateAdapter
import com.mobileforce.hometeach.ui.classes.parentstudent.ParentOngoingFragment
import com.mobileforce.hometeach.ui.classes.parentstudent.ParentRequestFragment
import com.mobileforce.hometeach.ui.classes.parentstudent.ParentStudentClassFragment

/**
 * Created by Mayokun Adeniyi on 27/06/2020.
 */

class ParentViewPagerFragmentAdapter(fragment: ParentStudentClassFragment) :
    FragmentStateAdapter(fragment) {
    override fun getItemCount(): Int = 2

    override fun createFragment(position: Int): Fragment {
        return when (position) {
            0 -> {
                ParentRequestFragment()
            }
            1 -> {
                ParentOngoingFragment()
            }
            else -> ParentRequestFragment()
        }
    }
}