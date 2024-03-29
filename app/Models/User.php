<?php

namespace App\Models;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Cashier\Billable;

class User extends Authenticatable
{
    use HasFactory, Notifiable,Billable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name',
        'email',
        'password',
        'provider',
        'provider_id',
        'provider_token'
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
    ];
    public function profile()
    {
      return $this->hasOne(Profile::class);  
    }
    public function cart()
    {
      return$this->hasOne(Cart::class);
    }
    public function products()
    {
       return $this->hasMany(Product::class);
    }
    public function orders()
    {
       return $this->belongsToMany(Order::class)->withPivot(['quantity']); 
    }
    public function categories()
    {
      return $this->belongsToMany(Category::class);
    }
}
