package com.telusko.demo;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HomeController
{
	@RequestMapping("home")//this is a request called home
	public ModelAndView home(Alien alien)
	//An object can be passed into the function home
	
	{
		ModelAndView mv= new ModelAndView();
		mv.addObject("obj", alien);
		mv.setViewName("home");
//		spring modelandview gives you and view and a view name
		return mv;
	}
}
